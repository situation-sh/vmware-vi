# IscsiFaultVnicAlreadyBound

This fault indicates that the given Virtual NIC is already bound to the iSCSI HBA.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vnic_device** | **str** |  | 

## Example

```python
from vmware_vi.models.iscsi_fault_vnic_already_bound import IscsiFaultVnicAlreadyBound

# TODO update the JSON string below
json = "{}"
# create an instance of IscsiFaultVnicAlreadyBound from a JSON string
iscsi_fault_vnic_already_bound_instance = IscsiFaultVnicAlreadyBound.from_json(json)
# print the JSON string representation of the object
print IscsiFaultVnicAlreadyBound.to_json()

# convert the object into a dict
iscsi_fault_vnic_already_bound_dict = iscsi_fault_vnic_already_bound_instance.to_dict()
# create an instance of IscsiFaultVnicAlreadyBound from a dict
iscsi_fault_vnic_already_bound_form_dict = iscsi_fault_vnic_already_bound.from_dict(iscsi_fault_vnic_already_bound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


