import os
import json
from nose.tools import assert_equal, assert_in

class TestValidation:

  dirs = [
    os.path.abspath(os.path.join(__file__, '../../','top_topics'))
  ];

  json_files = [
    os.path.abspath(os.path.join(__file__, '../../','top_topics/top_topics_multilingual.json')),
    os.path.abspath(os.path.join(__file__, '../../','taxonomy_en.json')),
    os.path.abspath(os.path.join(__file__, '../../','taxonomy_km.json')),
    os.path.abspath(os.path.join(__file__, '../../','taxonomy_th.json')),
    os.path.abspath(os.path.join(__file__, '../../','taxonomy_vi.json'))
  ];

  def test_01_data_available(self):

    for directory in self.dirs:
      assert os.path.isdir(directory)

    for json_file in self.json_files:
      assert os.path.isfile(json_file)

  def test_02_correct_json_files(self):

    all_valid = True
    for json_file in self.json_files:
      with open(json_file) as f:
        try:
          return json.loads(f.read())
        except ValueError as e:
          all_valid = False
          print('invalid json: %s' % e)

      assert all_valid
