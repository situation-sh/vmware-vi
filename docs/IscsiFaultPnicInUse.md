# IscsiFaultPnicInUse

This fault indicates the given Physical NIC is being used by iSCSI HBA.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pnic_device** | **str** |  | 

## Example

```python
from vmware_vi.models.iscsi_fault_pnic_in_use import IscsiFaultPnicInUse

# TODO update the JSON string below
json = "{}"
# create an instance of IscsiFaultPnicInUse from a JSON string
iscsi_fault_pnic_in_use_instance = IscsiFaultPnicInUse.from_json(json)
# print the JSON string representation of the object
print IscsiFaultPnicInUse.to_json()

# convert the object into a dict
iscsi_fault_pnic_in_use_dict = iscsi_fault_pnic_in_use_instance.to_dict()
# create an instance of IscsiFaultPnicInUse from a dict
iscsi_fault_pnic_in_use_form_dict = iscsi_fault_pnic_in_use.from_dict(iscsi_fault_pnic_in_use_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


