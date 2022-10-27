$(function () {
  $('#btn_search').click(function () {
    $.get('https://www.fourtonfish.com/hellosalut/hello/' + $('#city_search').val() + '%22)&format=json', function (data, textStatus) {
      if (textStatus === 'success' && data.query.results !== null) {
        $('#wind_speed').text(data.query.results.channel.wind.speed);
      } else {
        $('#wind_speed').text('Invalid city');
      }
    });
  });
});
