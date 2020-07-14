my_dict = {'resources' :[{
    'keyId': '0215a1bf-c82d-43aa-ab00-47201d99d4fd',
    'resourceCrn': 'crn:v1:staging:public:kms:us-south:a/6ceec6b5a7f22aa73df8c87288568c8d:e46843d9-6378-479d-bf97-b12ed40e544a:93b518ef-5c8d-4b81-b402-2be0b72dc80b:JbsVwycu',
    'createdBy': 'crn-crn:v1:staging:public:kms:us-south:a/6ceec6b5a7f22aa73df8c87288568c8d:e46843d9-6378-479d-bf97-b12ed40e544a::',
    'creationDate': '2020-04-16T23:07:52Z',
    'lastUpdated': '2020-04-16T23:07:52Z',
    'description': 'some description',
    'registrationMetadata': 'some registration metadata',
    'preventKeyDeletion': True,
    'keyVersion': {
      'id': '0215a1bf-c82d-43aa-ab00-47201d99d4fd',
      'creationDate': '2020-04-16T23:07:50Z'
    }
  }, {
    'keyId': '3bb28494-bc1f-4524-b8ae-665bfa29807c',
    'resourceCrn': 'crn:v1:staging:public:kms:us-south:a/6ceec6b5a7f22aa73df8c87288568c8d:e46843d9-6378-479d-bf97-b12ed40e544a:93b518ef-5c8d-4b81-b402-2be0b72dc80b:JbsVwycu',
    'createdBy': 'crn-crn:v1:staging:public:kms:us-south:a/6ceec6b5a7f22aa73df8c87288568c8d:e46843d9-6378-479d-bf97-b12ed40e544a::',
    'creationDate': '2020-04-16T23:07:51Z',
    'lastUpdated': '2020-04-16T23:07:51Z',
    'description': 'some description',
    'registrationMetadata': 'some registration metadata',
    'preventKeyDeletion': True,
    'keyVersion': {
      'id': '3bb28494-bc1f-4524-b8ae-665bfa29807c',
      'creationDate': '2020-04-16T23:07:50Z'
    }
  }]
}



for index in range(len(my_dict['resources'])):
     print(my_dict['resources'][index]['preventKeyDeletion'])
        



