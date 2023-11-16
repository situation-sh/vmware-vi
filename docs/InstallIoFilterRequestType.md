# InstallIoFilterRequestType

The parameters of *IoFilterManager.InstallIoFilter_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vib_url** | **str** | The URL that points to the IO Filter VIB package.  | 
**comp_res** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.install_io_filter_request_type import InstallIoFilterRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of InstallIoFilterRequestType from a JSON string
install_io_filter_request_type_instance = InstallIoFilterRequestType.from_json(json)
# print the JSON string representation of the object
print InstallIoFilterRequestType.to_json()

# convert the object into a dict
install_io_filter_request_type_dict = install_io_filter_request_type_instance.to_dict()
# create an instance of InstallIoFilterRequestType from a dict
install_io_filter_request_type_form_dict = install_io_filter_request_type.from_dict(install_io_filter_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


