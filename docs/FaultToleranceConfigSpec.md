# FaultToleranceConfigSpec

FaultToleranceConfigSpec contains information about the metadata file and vmdk files for a fault tolerant VM pair.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta_data_path** | [**FaultToleranceMetaSpec**](FaultToleranceMetaSpec.md) |  | [optional] 
**secondary_vm_spec** | [**FaultToleranceVMConfigSpec**](FaultToleranceVMConfigSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.fault_tolerance_config_spec import FaultToleranceConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of FaultToleranceConfigSpec from a JSON string
fault_tolerance_config_spec_instance = FaultToleranceConfigSpec.from_json(json)
# print the JSON string representation of the object
print FaultToleranceConfigSpec.to_json()

# convert the object into a dict
fault_tolerance_config_spec_dict = fault_tolerance_config_spec_instance.to_dict()
# create an instance of FaultToleranceConfigSpec from a dict
fault_tolerance_config_spec_form_dict = fault_tolerance_config_spec.from_dict(fault_tolerance_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


