# EnableMultipathPathRequestType

The parameters of *HostStorageSystem.EnableMultipathPath*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path_name** | **str** | The name of the path to enable.  | 

## Example

```python
from vmware_vi.models.enable_multipath_path_request_type import EnableMultipathPathRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of EnableMultipathPathRequestType from a JSON string
enable_multipath_path_request_type_instance = EnableMultipathPathRequestType.from_json(json)
# print the JSON string representation of the object
print EnableMultipathPathRequestType.to_json()

# convert the object into a dict
enable_multipath_path_request_type_dict = enable_multipath_path_request_type_instance.to_dict()
# create an instance of EnableMultipathPathRequestType from a dict
enable_multipath_path_request_type_form_dict = enable_multipath_path_request_type.from_dict(enable_multipath_path_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


