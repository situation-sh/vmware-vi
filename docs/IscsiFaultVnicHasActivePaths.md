# IscsiFaultVnicHasActivePaths

This fault indicates the given Virtual NIC has active storage paths associated with it.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vnic_device** | **str** |  | 

## Example

```python
from vmware_vi.models.iscsi_fault_vnic_has_active_paths import IscsiFaultVnicHasActivePaths

# TODO update the JSON string below
json = "{}"
# create an instance of IscsiFaultVnicHasActivePaths from a JSON string
iscsi_fault_vnic_has_active_paths_instance = IscsiFaultVnicHasActivePaths.from_json(json)
# print the JSON string representation of the object
print IscsiFaultVnicHasActivePaths.to_json()

# convert the object into a dict
iscsi_fault_vnic_has_active_paths_dict = iscsi_fault_vnic_has_active_paths_instance.to_dict()
# create an instance of IscsiFaultVnicHasActivePaths from a dict
iscsi_fault_vnic_has_active_paths_form_dict = iscsi_fault_vnic_has_active_paths.from_dict(iscsi_fault_vnic_has_active_paths_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


