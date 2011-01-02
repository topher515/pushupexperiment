from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse

def huh(request):
	
	return render_to_response('huh.html',{},RequestContext(request))