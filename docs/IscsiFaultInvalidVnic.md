# IscsiFaultInvalidVnic

This fault indicates an attempt is made to bind a Virtual NIC to an iSCSI adapter where the Virtual NIC has no association with the adapter.  For ex: The uplink for the given Virtual NIC is not valid for the iSCSI HBA.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vnic_device** | **str** |  | 

## Example

```python
from vmware_vi.models.iscsi_fault_invalid_vnic import IscsiFaultInvalidVnic

# TODO update the JSON string below
json = "{}"
# create an instance of IscsiFaultInvalidVnic from a JSON string
iscsi_fault_invalid_vnic_instance = IscsiFaultInvalidVnic.from_json(json)
# print the JSON string representation of the object
print IscsiFaultInvalidVnic.to_json()

# convert the object into a dict
iscsi_fault_invalid_vnic_dict = iscsi_fault_invalid_vnic_instance.to_dict()
# create an instance of IscsiFaultInvalidVnic from a dict
iscsi_fault_invalid_vnic_form_dict = iscsi_fault_invalid_vnic.from_dict(iscsi_fault_invalid_vnic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


