# KeyNotFound

An KeyNotFound fault is returned when the key does not exist among key value pairs.  ***Since:*** vSphere API 6.7.2 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The non existing key.  ***Since:*** vSphere API 6.7.2  | 

## Example

```python
from vmware_vi.models.key_not_found import KeyNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of KeyNotFound from a JSON string
key_not_found_instance = KeyNotFound.from_json(json)
# print the JSON string representation of the object
print KeyNotFound.to_json()

# convert the object into a dict
key_not_found_dict = key_not_found_instance.to_dict()
# create an instance of KeyNotFound from a dict
key_not_found_form_dict = key_not_found.from_dict(key_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


