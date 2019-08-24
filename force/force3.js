// This is adapted from https://bl.ocks.org/mbostock/2675ff61ea5e063ede2b5d63c08020c7

var svg3 = d3.select("#svg3"),
    width = +svg3.attr("width"),
    height = +svg3.attr("height");

//d3.select('body').append('svg3')
var simulation3 = d3.forceSimulation(svg3)
    .force("link", d3.forceLink().id(function (d) {
        return d.id;
    }))
    .force("charge", d3.forceManyBody())
    .force("center", d3.forceCenter(width / 2, height / 2));

d3.json("force/region_3_old.json", function (error, graph3) {
    if (error) throw error;

    var link = svg3.append("g")
        .attr("class", "links")
//        .attr('fill', 'red')
//        .attr('stroke', 'red')
//        //.attr('stroke-width', function(d) { return d.weight; })
//        .attr("stroke-width", function(d) { return  d.weight;})
        .selectAll("line")
        .data(graph3.links)
        .enter().append("line");

    var node = svg3.append("g")
        .attr("class", "nodes")
        .selectAll("circle")
        .data(graph3.nodes)
        .enter().append("circle")
        .style("fill", function(d) {
        if (d.class == 1)
        return 'red'
        else
        return 'blue';
  })
        .attr("r", function(d) {
        if (d.degree >= 20 ){return 15}
        else if (d.degree < 20 && d.degree >= 16) {return 12}
        else if (d.degree < 16 && d.degree > 9) {return 10}
        else return d.degree;
  })
        .call(d3.drag()
            .on("start", dragstarted3)
            .on("drag", dragged3)
            .on("end", dragended3));

    node.append("title")
        .text(function (d) {
            return d.id;
        });

    simulation3
        .nodes(graph3.nodes)
        .on("tick", ticked);

    simulation3.force("link")
        .links(graph3.links);

    function ticked() {
        link
            .attr("x1", function (d) {
                return d.source.x;
            })
            .attr("y1", function (d) {
                return d.source.y;
            })
            .attr("x2", function (d) {
                return d.target.x;
            })
            .attr("y2", function (d) {
                return d.target.y;
            });

        node
            .attr("cx", function (d) {
                return d.x;
            })
            .attr("cy", function (d) {
                return d.y;
            });
    }
});

function dragstarted3(d) {
    if (!d3.event.active) simulation3.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
}

function dragged3(d) {
    d.fx = d3.event.x;
    d.fy = d3.event.y;
}

function dragended3(d) {
    if (!d3.event.active) simulation3.alphaTarget(0);
    d.fx = null;
    d.fy = null;
}