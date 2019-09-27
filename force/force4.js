// This is adapted from https://bl.ocks.org/mbostock/2675ff61ea5e063ede2b5d63c08020c7

var svg4 = d3.select("#svg4"),
    width = +svg4.attr("width"),
    height = +svg4.attr("height");

var simulation4 = d3.forceSimulation(svg4)
    .force("link", d3.forceLink().id(function (d) {
        return d.id;
    }))
    .force("charge", d3.forceManyBody())
    .force("center", d3.forceCenter(width / 2, height / 2));

d3.json("force/region_4_old.json", function (error, graph4) {
    if (error) throw error;

    var link = svg4.append("g")
        .attr("class", "links")
        .selectAll("line")
        .data(graph4.links)
        .enter().append("line");

    var node = svg4.append("g")
        .attr("class", "nodes")
        .selectAll("circle")
        .data(graph4.nodes)
        .enter().append("circle")
        .style("fill", function(d) {
        if (d.class == 1)
        return 'red'
        else
        return 'blue';
  })
        .attr("r", function(d) {
        if (d.betweenness >= 20 ){return 15}
        else if (d.betweenness < 20 && d.betweenness >= 16) {return 12}
        else if (d.betweenness < 16 && d.betweenness > 9) {return 10}
        else return d.betweenness;
  })
        .call(d3.drag()
            .on("start", dragstarted4)
            .on("drag", dragged4)
            .on("end", dragended4));

    node.append("title")
        .text(function (d) {
            return d.id;
        });

    simulation4
        .nodes(graph4.nodes)
        .on("tick", ticked);

    simulation4.force("link")
        .links(graph4.links);

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

function dragstarted4(d) {
    if (!d3.event.active) simulation4.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
}

function dragged4(d) {
    d.fx = d3.event.x;
    d.fy = d3.event.y;
}

function dragended4(d) {
    if (!d3.event.active) simulation4.alphaTarget(0);
    d.fx = null;
    d.fy = null;
}