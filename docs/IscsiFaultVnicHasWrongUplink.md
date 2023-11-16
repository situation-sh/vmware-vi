# IscsiFaultVnicHasWrongUplink

This fault indicates the given Virtual NIC has the wrong Physical uplink for iSCSI multi-pathing configuration.  The Physical uplink is not associated with the iSCSI Host Bus Adapter.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vnic_device** | **str** | Contains the VMkernel virtual NIC device name.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.iscsi_fault_vnic_has_wrong_uplink import IscsiFaultVnicHasWrongUplink

# TODO update the JSON string below
json = "{}"
# create an instance of IscsiFaultVnicHasWrongUplink from a JSON string
iscsi_fault_vnic_has_wrong_uplink_instance = IscsiFaultVnicHasWrongUplink.from_json(json)
# print the JSON string representation of the object
print IscsiFaultVnicHasWrongUplink.to_json()

# convert the object into a dict
iscsi_fault_vnic_has_wrong_uplink_dict = iscsi_fault_vnic_has_wrong_uplink_instance.to_dict()
# create an instance of IscsiFaultVnicHasWrongUplink from a dict
iscsi_fault_vnic_has_wrong_uplink_form_dict = iscsi_fault_vnic_has_wrong_uplink.from_dict(iscsi_fault_vnic_has_wrong_uplink_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


