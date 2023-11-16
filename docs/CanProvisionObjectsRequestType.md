# CanProvisionObjectsRequestType

The parameters of *HostVsanInternalSystem.CanProvisionObjects*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**npbs** | [**List[VsanNewPolicyBatch]**](VsanNewPolicyBatch.md) | List of NewPolicyBatch structure with sizes and policies.  ***Since:*** vSphere API 5.5  | 
**ignore_satisfiability** | **bool** | Optionally populate PolicyCost even though object cannot be provisioned in the current cluster topology.  | [optional] 

## Example

```python
from vmware_vi.models.can_provision_objects_request_type import CanProvisionObjectsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CanProvisionObjectsRequestType from a JSON string
can_provision_objects_request_type_instance = CanProvisionObjectsRequestType.from_json(json)
# print the JSON string representation of the object
print CanProvisionObjectsRequestType.to_json()

# convert the object into a dict
can_provision_objects_request_type_dict = can_provision_objects_request_type_instance.to_dict()
# create an instance of CanProvisionObjectsRequestType from a dict
can_provision_objects_request_type_form_dict = can_provision_objects_request_type.from_dict(can_provision_objects_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


