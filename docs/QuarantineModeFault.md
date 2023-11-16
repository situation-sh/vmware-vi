# QuarantineModeFault


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm_name** | **str** |  | 
**fault_type** | **str** |  | 

## Example

```python
from vmware_vi.models.quarantine_mode_fault import QuarantineModeFault

# TODO update the JSON string below
json = "{}"
# create an instance of QuarantineModeFault from a JSON string
quarantine_mode_fault_instance = QuarantineModeFault.from_json(json)
# print the JSON string representation of the object
print QuarantineModeFault.to_json()

# convert the object into a dict
quarantine_mode_fault_dict = quarantine_mode_fault_instance.to_dict()
# create an instance of QuarantineModeFault from a dict
quarantine_mode_fault_form_dict = quarantine_mode_fault.from_dict(quarantine_mode_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


