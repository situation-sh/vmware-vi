# FaultToleranceMetaSpec

This data object encapsulates the Datastore for the shared metadata file for a fault tolerant pair of VMs.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta_data_datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.fault_tolerance_meta_spec import FaultToleranceMetaSpec

# TODO update the JSON string below
json = "{}"
# create an instance of FaultToleranceMetaSpec from a JSON string
fault_tolerance_meta_spec_instance = FaultToleranceMetaSpec.from_json(json)
# print the JSON string representation of the object
print FaultToleranceMetaSpec.to_json()

# convert the object into a dict
fault_tolerance_meta_spec_dict = fault_tolerance_meta_spec_instance.to_dict()
# create an instance of FaultToleranceMetaSpec from a dict
fault_tolerance_meta_spec_form_dict = fault_tolerance_meta_spec.from_dict(fault_tolerance_meta_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


