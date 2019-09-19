// This is adapted from https://bl.ocks.org/mbostock/2675ff61ea5e063ede2b5d63c08020c7

var svg3_new = d3.select("#svg3_new"),
    width = +svg3_new.attr("width"),
    height = +svg3_new.attr("height");

var simulation3_new = d3.forceSimulation(svg3_new)
    .force("link", d3.forceLink().id(function (d) {
        return d.id;
    }))
    .force("charge", d3.forceManyBody())
    .force("center", d3.forceCenter(width / 2, height / 2));

d3.json("force/region_3_new.json", function (error, graph3_new) {
    if (error) throw error;

    var link = svg3_new.append("g")
        .attr("class", "links")
        .selectAll("line")
        .data(graph3_new.links)
        .enter().append("line");

    var node = svg3_new.append("g")
        .attr("class", "nodes")
        .selectAll("circle")
        .data(graph3_new.nodes)
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
            .on("start", dragstarted3_new)
            .on("drag", dragged3_new)
            .on("end", dragended3_new));

    node.append("title")
        .text(function (d) {
            return d.id;
        });

    simulation3_new
        .nodes(graph3_new.nodes)
        .on("tick", ticked);

    simulation3_new.force("link")
        .links(graph3_new.links);

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

function dragstarted3_new(d) {
    if (!d3.event.active) simulation3_new.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
}

function dragged3_new(d) {
    d.fx = d3.event.x;
    d.fy = d3.event.y;
}

function dragended3_new(d) {
    if (!d3.event.active) simulation3_new.alphaTarget(0);
    d.fx = null;
    d.fy = null;
}
