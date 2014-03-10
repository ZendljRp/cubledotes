class Wall

  endpoint = "https://api.instagram.com/v1/"

  constructor: (@selector, @access_token) ->
    @container= $(@selector)
    @stream = []
    ww = $(window).width()

    request = $.ajax
      url : "#{@endpoint}users/self/media/recent?access_token=#{@access_token}&max_timestamp=0"
      dataType: "jsonp"
    request.done (response) =>
      for photo in response.data
        requset = $.ajax
          url : "#{@endpoint}media/#{photo.id}?access_token=#{@access_token}"
          dataType: "jsonp"
        request.done (data) =>
          @stream.push data
