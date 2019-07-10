#!/usr/bin/env python

"""

Makes a file hierarchy.json, in the current directory:

{ 'tag_to_path': { "english tag as in ckan": "#,#", // path as numbers, comma separated
                   "tag": "#,#,#",
                 ... },
  'translations': { '#,#,#': {'en': 'tag in en',
                              'km': 'tag in km',
                              'lo': 'tag in lo',
                             ... },
                  }
}

Ckan returns english tag names. These names aren't associated with any hierarchy in ckan.
There are translations in the database, but we need to get translations of terms
up the hierarchy that aren't necessarily going to show up in the response.

The path as numbers can be converted to a list by split, then trimmed to length to
find the first n levels of path components, to then get the translated category names

"""

import collections
import json

def collect_path(elt, path):
   ret = [(tuple(path), elt['name'])]
   for ix, child in enumerate(elt.get('children',[])):
     ret.extend(collect_path(child, path + [ix]))
   return ret

def generate(langs):
   translations = collections.defaultdict(dict)
   for lang in langs:
      with open('taxonomy_%s.json' % lang) as f:
         src = json.load(f)
      transformed = collect_path(src, [])
      for k, v in transformed:
         translations[','.join(str(p) for p in k)][lang] = v
   forward = {v['en']:k for k,v in translations.items()}

   return { 'translations': translations,
            'tag_to_path': forward }

with open('hierarchy.json', 'w') as f:
   json.dump(generate(('en', 'km', 'lo', 'my', 'th', 'vi')), f)
