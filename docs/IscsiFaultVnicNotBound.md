# IscsiFaultVnicNotBound

This fault indicates an attempt was made to remove a Virtual NIC from an iSCSI HBA while Virtual NIC is not associated with the adapter.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vnic_device** | **str** |  | 

## Example

```python
from vmware_vi.models.iscsi_fault_vnic_not_bound import IscsiFaultVnicNotBound

# TODO update the JSON string below
json = "{}"
# create an instance of IscsiFaultVnicNotBound from a JSON string
iscsi_fault_vnic_not_bound_instance = IscsiFaultVnicNotBound.from_json(json)
# print the JSON string representation of the object
print IscsiFaultVnicNotBound.to_json()

# convert the object into a dict
iscsi_fault_vnic_not_bound_dict = iscsi_fault_vnic_not_bound_instance.to_dict()
# create an instance of IscsiFaultVnicNotBound from a dict
iscsi_fault_vnic_not_bound_form_dict = iscsi_fault_vnic_not_bound.from_dict(iscsi_fault_vnic_not_bound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


