// This is adapted from https://bl.ocks.org/mbostock/2675ff61ea5e063ede2b5d63c08020c7

var svg4_new = d3.select("#svg4_new"),
    width = +svg4_new.attr("width"),
    height = +svg4_new.attr("height");

//d3.select('body').append('svg4_new')
var simulation4_new = d3.forceSimulation(svg4_new)
    .force("link", d3.forceLink().id(function (d) {
        return d.id;
    }))
    .force("charge", d3.forceManyBody())
    .force("center", d3.forceCenter(width / 2, height / 2));

d3.json("force/region_4_new.json", function (error, graph4_new) {
    if (error) throw error;

    var link = svg4_new.append("g")
        .attr("class", "links")
//        .attr('fill', 'red')
//        .attr('stroke', 'red')
//        //.attr('stroke-width', function(d) { return d.weight; })
//        .attr("stroke-width", function(d) { return  d.weight;})
        .selectAll("line")
        .data(graph4_new.links)
        .enter().append("line");

    var node = svg4_new.append("g")
        .attr("class", "nodes")
        .selectAll("circle")
        .data(graph4_new.nodes)
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
            .on("start", dragstarted4_new)
            .on("drag", dragged4_new)
            .on("end", dragended4_new));

    node.append("title")
        .text(function (d) {
            return d.id;
        });

//    var label = svg2_new.selectAll("nodes")
//    .data(graph4_new.nodes)
//    .enter()
//    .append("text")
//    .text(function (d) { return d.id; })
//    .style("text-anchor", "middle")
//    .style("fill", "#555")
//    .style("font-family", "Arial")
//    .style("font-size", 9);

    simulation4_new
        .nodes(graph4_new.nodes)
        .on("tick", ticked);

    simulation4_new.force("link")
        .links(graph4_new.links);

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

//        label.attr("x", function(d){ return d.x; })
//    			 .attr("y", function (d) {return d.y - 10; });
    }
});

function dragstarted4_new(d) {
    if (!d3.event.active) simulation4_new.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
}

function dragged4_new(d) {
    d.fx = d3.event.x;
    d.fy = d3.event.y;
}

function dragended4_new(d) {
    if (!d3.event.active) simulation4_new.alphaTarget(0);
    d.fx = null;
    d.fy = null;
}
