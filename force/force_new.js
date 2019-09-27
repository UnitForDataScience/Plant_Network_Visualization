// This is adapted from https://bl.ocks.org/mbostock/2675ff61ea5e063ede2b5d63c08020c7

var svg1_new = d3.select("#svg1_new"),
    width = +svg1_new.attr("width"),
    height = +svg1_new.attr("height");

var simulation_new = d3.forceSimulation(svg1_new)
    .force("link", d3.forceLink().id(function (d) {
        return d.id;
    }))
    .force("charge", d3.forceManyBody())
    .force("center", d3.forceCenter(width / 2, height / 2));

d3.json("force/region_1_new.json", function (error, graph_new) {
    if (error) throw error;

    var link = svg1_new.append("g")
        .attr("class", "links")
        .selectAll("line")
        .data(graph_new.links)
        .enter().append("line");

    var node = svg1_new.append("g")
        .attr("class", "nodes")
        .selectAll("circle")
        .data(graph_new.nodes)
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
            .on("start", dragstarted_new)
            .on("drag", dragged_new)
            .on("end", dragended_new));

    node.append("title")
        .text(function (d) {
            return d.id;
        });

    simulation_new
        .nodes(graph_new.nodes)
        .on("tick", ticked);

    simulation_new.force("link")
        .links(graph_new.links);

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

function dragstarted_new(d) {
    if (!d3.event.active) simulation_new.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
}

function dragged_new(d) {
    d.fx = d3.event.x;
    d.fy = d3.event.y;
}

function dragended_new(d) {
    if (!d3.event.active) simulation_new.alphaTarget(0);
    d.fx = null;
    d.fy = null;
}