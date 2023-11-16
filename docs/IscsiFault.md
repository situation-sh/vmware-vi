# IscsiFault

Base class for faults that can be thrown while invoking iSCSI management operations.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.iscsi_fault import IscsiFault

# TODO update the JSON string below
json = "{}"
# create an instance of IscsiFault from a JSON string
iscsi_fault_instance = IscsiFault.from_json(json)
# print the JSON string representation of the object
print IscsiFault.to_json()

# convert the object into a dict
iscsi_fault_dict = iscsi_fault_instance.to_dict()
# create an instance of IscsiFault from a dict
iscsi_fault_form_dict = iscsi_fault.from_dict(iscsi_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


