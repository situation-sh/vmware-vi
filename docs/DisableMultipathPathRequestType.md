# DisableMultipathPathRequestType

The parameters of *HostStorageSystem.DisableMultipathPath*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path_name** | **str** | The name of the path to disable.  | 

## Example

```python
from vmware_vi.models.disable_multipath_path_request_type import DisableMultipathPathRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DisableMultipathPathRequestType from a JSON string
disable_multipath_path_request_type_instance = DisableMultipathPathRequestType.from_json(json)
# print the JSON string representation of the object
print DisableMultipathPathRequestType.to_json()

# convert the object into a dict
disable_multipath_path_request_type_dict = disable_multipath_path_request_type_instance.to_dict()
# create an instance of DisableMultipathPathRequestType from a dict
disable_multipath_path_request_type_form_dict = disable_multipath_path_request_type.from_dict(disable_multipath_path_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


