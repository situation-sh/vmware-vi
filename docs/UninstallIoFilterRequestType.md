# UninstallIoFilterRequestType

The parameters of *IoFilterManager.UninstallIoFilter_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_id** | **str** | ID of the filter.  | 
**comp_res** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.uninstall_io_filter_request_type import UninstallIoFilterRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UninstallIoFilterRequestType from a JSON string
uninstall_io_filter_request_type_instance = UninstallIoFilterRequestType.from_json(json)
# print the JSON string representation of the object
print UninstallIoFilterRequestType.to_json()

# convert the object into a dict
uninstall_io_filter_request_type_dict = uninstall_io_filter_request_type_instance.to_dict()
# create an instance of UninstallIoFilterRequestType from a dict
uninstall_io_filter_request_type_form_dict = uninstall_io_filter_request_type.from_dict(uninstall_io_filter_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


