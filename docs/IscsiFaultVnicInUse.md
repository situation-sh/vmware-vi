# IscsiFaultVnicInUse

This fault indicates the given Virtual NIC is being used by iSCSI and the requested operation can't be completed.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vnic_device** | **str** |  | 

## Example

```python
from vmware_vi.models.iscsi_fault_vnic_in_use import IscsiFaultVnicInUse

# TODO update the JSON string below
json = "{}"
# create an instance of IscsiFaultVnicInUse from a JSON string
iscsi_fault_vnic_in_use_instance = IscsiFaultVnicInUse.from_json(json)
# print the JSON string representation of the object
print IscsiFaultVnicInUse.to_json()

# convert the object into a dict
iscsi_fault_vnic_in_use_dict = iscsi_fault_vnic_in_use_instance.to_dict()
# create an instance of IscsiFaultVnicInUse from a dict
iscsi_fault_vnic_in_use_form_dict = iscsi_fault_vnic_in_use.from_dict(iscsi_fault_vnic_in_use_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


