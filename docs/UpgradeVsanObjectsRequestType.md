# UpgradeVsanObjectsRequestType

The parameters of *HostVsanInternalSystem.UpgradeVsanObjects*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuids** | **List[str]** | The array of objects&#39; UUID which will be upgraded.  | 
**new_version** | **int** | The new version will be applied to objects.  | 

## Example

```python
from vmware_vi.models.upgrade_vsan_objects_request_type import UpgradeVsanObjectsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeVsanObjectsRequestType from a JSON string
upgrade_vsan_objects_request_type_instance = UpgradeVsanObjectsRequestType.from_json(json)
# print the JSON string representation of the object
print UpgradeVsanObjectsRequestType.to_json()

# convert the object into a dict
upgrade_vsan_objects_request_type_dict = upgrade_vsan_objects_request_type_instance.to_dict()
# create an instance of UpgradeVsanObjectsRequestType from a dict
upgrade_vsan_objects_request_type_form_dict = upgrade_vsan_objects_request_type.from_dict(upgrade_vsan_objects_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


