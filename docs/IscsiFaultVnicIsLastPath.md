# IscsiFaultVnicIsLastPath

This fault indicates that the given Virtual NIC is associated with the only path to the storage.  Any attempt to unbind this from iSCSI HBA would result in storage being inaccessible.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vnic_device** | **str** |  | 

## Example

```python
from vmware_vi.models.iscsi_fault_vnic_is_last_path import IscsiFaultVnicIsLastPath

# TODO update the JSON string below
json = "{}"
# create an instance of IscsiFaultVnicIsLastPath from a JSON string
iscsi_fault_vnic_is_last_path_instance = IscsiFaultVnicIsLastPath.from_json(json)
# print the JSON string representation of the object
print IscsiFaultVnicIsLastPath.to_json()

# convert the object into a dict
iscsi_fault_vnic_is_last_path_dict = iscsi_fault_vnic_is_last_path_instance.to_dict()
# create an instance of IscsiFaultVnicIsLastPath from a dict
iscsi_fault_vnic_is_last_path_form_dict = iscsi_fault_vnic_is_last_path.from_dict(iscsi_fault_vnic_is_last_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


