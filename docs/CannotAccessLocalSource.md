# CannotAccessLocalSource

An CannotAccessLocalSourceFault exception is thrown when a an attempt is made to upload license content and the local source cannot be accesed. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.cannot_access_local_source import CannotAccessLocalSource

# TODO update the JSON string below
json = "{}"
# create an instance of CannotAccessLocalSource from a JSON string
cannot_access_local_source_instance = CannotAccessLocalSource.from_json(json)
# print the JSON string representation of the object
print CannotAccessLocalSource.to_json()

# convert the object into a dict
cannot_access_local_source_dict = cannot_access_local_source_instance.to_dict()
# create an instance of CannotAccessLocalSource from a dict
cannot_access_local_source_form_dict = cannot_access_local_source.from_dict(cannot_access_local_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


