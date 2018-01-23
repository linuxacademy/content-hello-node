require 'rubygems'
require 'bundler'

Bundler.require

require './app.rv'

run Sinatra::Application
