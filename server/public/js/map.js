google.charts.load('current', {packages: ['corechart']});

var width = 960,

    height = 1160;


function percentages(res) {
var sum = 0;
res.map(function (item) {
  sum += item;
});

res.map(function (item) {
  return item/sum*100;
})
console.log(res);
return res
}

function drawChart(res) {
  var chart = new google.visualization.PieChart(document.getElementById('content'));
  var data = new google.visualization.DataTable();
  res=percentages(res)
  var options ={
    title: 'Resut Breakdown',
    is3D : true
  };
  data.addColumn('string', 'Result');
  data.addColumn('number', 'Percentage');
  data.addRows([
    ['Win', res[0]],
    ['Draw', res[2]],
    ['Loss', res[1]],
    ]);


  chart.draw(data, options);


}
function zoomFunction() {
    d3.selectAll("path")
        .attr("transform",
            "translate(" + d3.event.translate +
            ") scale (" +
            d3.event.scale + ")");
}

var zoom = d3.behavior.zoom()
    .scaleExtent([0.2, 10])
    .on("zoom", zoomFunction);

var svg = d3.select('body').append('svg')
    .attr('height', height)
    .attr('width', width)
//    .call(zoom);


d3.json("/data/uk.json", function(error, uk) {
    if (error) return console.error(error);


    var subunits = topojson.feature(uk, uk.objects.subunits);
    var projection = d3.geo.albers()
        .center([4, 53.4])
        .rotate([4.4, 0])
        .parallels([50, 60])
        .scale(9400)
        .translate([width / 2, height / 2]);

    var path = d3.geo.path()
        .projection(projection);
    svg.append('path')
        .datum(subunits)
        .attr('d', path);

    svg.selectAll('.subunit')
        .data(topojson.feature(uk, uk.objects.subunits).features)
        .enter().append('path')
        .attr('class', function(d, i) {
            return 'subunit ' + d.id;
        })
        .attr('d', path);

    svg.append("path")
        .datum(topojson.mesh(uk, uk.objects.subunits, function(a, b) {
            return a !== b;
        }))
        .attr("d", path)
        .attr("class", "subunit-boundary");


    d3.json('/data/stadium-info.json', function(error, result) {

        if (error)
            console.error(error);

        var geoPath = d3.geo.path().projection(projection)

        svg.selectAll('.features')
            .data(result.features)
            .enter().append('path')
            .attr('class', 'feature')
            .attr('name', function(d) {

                return d.properties.name
            })
            .attr('homeof', function(d) {
                return d.properties.home

            })
            .style('stroke', 'green')
            .attr('d', geoPath)

        d3.select("svg")
            .selectAll(".feature")
            .on("mouseenter", function(obj) {

                tooltip = d3.select(".tooltip");

                var mouseCoords = d3.mouse(this.parentElement);
                tooltip.style('top', mouseCoords[1] - 100 + 'px')
                    .style('left', mouseCoords[0] + 'px')

                d3.select('#tname')
                    .text(obj.properties.home)

                d3.select('#stadiumname')
                    .text(obj.properties.name)
                tooltip.style("opacity", "1");

            })

        d3.select("svg")
            .selectAll(".feature")
            .on("mouseleave", function() {
                tooltip.style("opacity", "0");

            })


        $(".close").click(function() {

            $('#myModal').hide()

        })

        window.onclick = function() {
            $('#myModal').hide()

            $('#content').empty()
            $('.modal-content').empty()

        }
        d3.select("svg")
            .selectAll(".feature")
            .on("click", function(object) {

                var data = {
                    name: object.properties.name,
                    home: object.properties.home,
                    id: object.properties.id
                }
                $.ajax({
                    type: 'POST',
                    data: JSON.stringify(data),
                    contentType: "application/json",
                    url: 'https://farmhand.herokuapp.com/input',
                    success: function(data) {
                        console.log(data);

                        $modal = $(".modal-content")
                        head = $("<h1></h1>").text(data.teamName)
                                              .attr("align", "center")
                        sub =  $("<h2></h2>").text(data.stadium)
                                              .attr("align", "center")


                        d3.select('#myModal').style('display', 'block')

                        $modal.append(sub)
                          $modal.append(head)

                        drawChart([data.win, data.lose,data.draws]);


                    },
                    error: function(error) {
                        console.log("some error in fetching the notifications");
                        console.log(error);
                    }

                });

            })
    });

});
