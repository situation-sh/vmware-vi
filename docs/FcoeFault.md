# FcoeFault

Deprecated as of vSphere API 8.0. Software FCoE not supported.  Base class for faults that can be thrown while invoking FCoE management operations.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.fcoe_fault import FcoeFault

# TODO update the JSON string below
json = "{}"
# create an instance of FcoeFault from a JSON string
fcoe_fault_instance = FcoeFault.from_json(json)
# print the JSON string representation of the object
print FcoeFault.to_json()

# convert the object into a dict
fcoe_fault_dict = fcoe_fault_instance.to_dict()
# create an instance of FcoeFault from a dict
fcoe_fault_form_dict = fcoe_fault.from_dict(fcoe_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


