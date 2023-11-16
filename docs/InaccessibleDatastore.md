# InaccessibleDatastore

An InaccessibleDatastore exception is thrown if the datastore corresponding to the given datastore path isn't currently accessible. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** |  | [optional] 

## Example

```python
from vmware_vi.models.inaccessible_datastore import InaccessibleDatastore

# TODO update the JSON string below
json = "{}"
# create an instance of InaccessibleDatastore from a JSON string
inaccessible_datastore_instance = InaccessibleDatastore.from_json(json)
# print the JSON string representation of the object
print InaccessibleDatastore.to_json()

# convert the object into a dict
inaccessible_datastore_dict = inaccessible_datastore_instance.to_dict()
# create an instance of InaccessibleDatastore from a dict
inaccessible_datastore_form_dict = inaccessible_datastore.from_dict(inaccessible_datastore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


