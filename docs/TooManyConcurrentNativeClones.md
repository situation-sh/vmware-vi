# TooManyConcurrentNativeClones

Thrown if the number of levels in the snapshot tree exceeds the supported maximum.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.too_many_concurrent_native_clones import TooManyConcurrentNativeClones

# TODO update the JSON string below
json = "{}"
# create an instance of TooManyConcurrentNativeClones from a JSON string
too_many_concurrent_native_clones_instance = TooManyConcurrentNativeClones.from_json(json)
# print the JSON string representation of the object
print TooManyConcurrentNativeClones.to_json()

# convert the object into a dict
too_many_concurrent_native_clones_dict = too_many_concurrent_native_clones_instance.to_dict()
# create an instance of TooManyConcurrentNativeClones from a dict
too_many_concurrent_native_clones_form_dict = too_many_concurrent_native_clones.from_dict(too_many_concurrent_native_clones_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


