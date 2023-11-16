# IscsiFaultVnicHasMultipleUplinks

This fault indicates that the Virtual NIC has multiple uplinks and not suitable for iSCSI multi-pathing and can not be bound to iSCSI HBA.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vnic_device** | **str** |  | 

## Example

```python
from vmware_vi.models.iscsi_fault_vnic_has_multiple_uplinks import IscsiFaultVnicHasMultipleUplinks

# TODO update the JSON string below
json = "{}"
# create an instance of IscsiFaultVnicHasMultipleUplinks from a JSON string
iscsi_fault_vnic_has_multiple_uplinks_instance = IscsiFaultVnicHasMultipleUplinks.from_json(json)
# print the JSON string representation of the object
print IscsiFaultVnicHasMultipleUplinks.to_json()

# convert the object into a dict
iscsi_fault_vnic_has_multiple_uplinks_dict = iscsi_fault_vnic_has_multiple_uplinks_instance.to_dict()
# create an instance of IscsiFaultVnicHasMultipleUplinks from a dict
iscsi_fault_vnic_has_multiple_uplinks_form_dict = iscsi_fault_vnic_has_multiple_uplinks.from_dict(iscsi_fault_vnic_has_multiple_uplinks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


