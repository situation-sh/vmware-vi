# ReconfigurationSatisfiableRequestType

The parameters of *HostVsanInternalSystem.ReconfigurationSatisfiable*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pcbs** | [**List[VsanPolicyChangeBatch]**](VsanPolicyChangeBatch.md) | List of PolicyChangeBatch structure with uuids and policies.  ***Since:*** vSphere API 5.5  | 
**ignore_satisfiability** | **bool** | Optionally populate PolicyCost even though object cannot be reconfigured in the current cluster topology.  | [optional] 

## Example

```python
from vmware_vi.models.reconfiguration_satisfiable_request_type import ReconfigurationSatisfiableRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ReconfigurationSatisfiableRequestType from a JSON string
reconfiguration_satisfiable_request_type_instance = ReconfigurationSatisfiableRequestType.from_json(json)
# print the JSON string representation of the object
print ReconfigurationSatisfiableRequestType.to_json()

# convert the object into a dict
reconfiguration_satisfiable_request_type_dict = reconfiguration_satisfiable_request_type_instance.to_dict()
# create an instance of ReconfigurationSatisfiableRequestType from a dict
reconfiguration_satisfiable_request_type_form_dict = reconfiguration_satisfiable_request_type.from_dict(reconfiguration_satisfiable_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


