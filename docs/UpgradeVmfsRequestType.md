# UpgradeVmfsRequestType

The parameters of *HostStorageSystem.UpgradeVmfs*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vmfs_path** | **str** | The path of the VMFS.  | 

## Example

```python
from vmware_vi.models.upgrade_vmfs_request_type import UpgradeVmfsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeVmfsRequestType from a JSON string
upgrade_vmfs_request_type_instance = UpgradeVmfsRequestType.from_json(json)
# print the JSON string representation of the object
print UpgradeVmfsRequestType.to_json()

# convert the object into a dict
upgrade_vmfs_request_type_dict = upgrade_vmfs_request_type_instance.to_dict()
# create an instance of UpgradeVmfsRequestType from a dict
upgrade_vmfs_request_type_form_dict = upgrade_vmfs_request_type.from_dict(upgrade_vmfs_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


