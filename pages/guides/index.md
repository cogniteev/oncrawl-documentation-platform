---
title: Available Guides
last_update: October, 27, 2016
summary: "Overview of available guides"
sidebar: mydoc_sidebar
permalink: guides
folder: guides
toc: false
---
<div class="row">
{% assign sorted_pages = (site.pages | sort: 'complexity') %}
{% for page in sorted_pages %}
{% for tag in page.tags %}
{% if tag == "guide" %}
	<div class="col-md-3 col-sm-6">
		<div class="panel panel-default text-center">
			<div class="panel-heading">
			    <span class="fa-stack fa-5x">
			          <i class="fa fa-circle fa-stack-2x text-primary"></i>
			          <i class="fa {{ page.fa_icon or 'fa-database' }} fa-stack-1x fa-inverse"></i>
			    </span>
			</div>
			<div class="panel-body">
			    <h4>{{ page.title | remove: " Guide" }}</h4>
			    <p>{{ page.summary }}</p>
			    <a
			      href="{{ page.url | remove: "/" }}"
			      class="btn btn-primary">
			      Read Guide
		      </a>
			</div>
		</div>
	</div>
{% endif %}
{% endfor %}
{% endfor %}
</div>
