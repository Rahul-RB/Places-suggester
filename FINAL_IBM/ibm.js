var NaturalLanguageUnderstandingV1 = require('watson-developer-cloud/natural-language-understanding/v1.js');
var natural_language_understanding = new NaturalLanguageUnderstandingV1({'username': 'a79238a0-5e8d-4b5b-8101-825adeff273e','password': 'UmI06x7q7AYk','version_date': '2017-02-27'});


var parameters = {
  'text': 'A very beautiful place to stay happy and eat joyfully!',
  'features': {
    'entities': {
      'emotion': true,
      'sentiment': true,
      'limit': 2
    },
    'keywords': {
      'emotion': true,
      'sentiment': true,
      'limit': 2
    }
  }
}

natural_language_understanding.analyze(parameters, function(err, response) {
  if (err)
    console.log('error:', err);
  else
    console.log(JSON.stringify(response, null, 2));
});
