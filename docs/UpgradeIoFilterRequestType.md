# UpgradeIoFilterRequestType

The parameters of *IoFilterManager.UpgradeIoFilter_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_id** | **str** | The filter to be upgraded.  | 
**comp_res** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**vib_url** | **str** | The URL that points to the new IO Filter VIB package.  | 

## Example

```python
from vmware_vi.models.upgrade_io_filter_request_type import UpgradeIoFilterRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeIoFilterRequestType from a JSON string
upgrade_io_filter_request_type_instance = UpgradeIoFilterRequestType.from_json(json)
# print the JSON string representation of the object
print UpgradeIoFilterRequestType.to_json()

# convert the object into a dict
upgrade_io_filter_request_type_dict = upgrade_io_filter_request_type_instance.to_dict()
# create an instance of UpgradeIoFilterRequestType from a dict
upgrade_io_filter_request_type_form_dict = upgrade_io_filter_request_type.from_dict(upgrade_io_filter_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


