# ReconfigureComputeResourceRequestType

The parameters of *ComputeResource.ReconfigureComputeResource_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**ComputeResourceConfigSpec**](ComputeResourceConfigSpec.md) |  | 
**modify** | **bool** | Flag to specify whether the specification (\&quot;spec\&quot;) should be applied incrementally. If \&quot;modify\&quot; is false and the operation succeeds, then the configuration of the cluster matches the specification exactly; in this case any unset portions of the specification will result in unset or default portions of the configuration.  | 

## Example

```python
from vmware_vi.models.reconfigure_compute_resource_request_type import ReconfigureComputeResourceRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ReconfigureComputeResourceRequestType from a JSON string
reconfigure_compute_resource_request_type_instance = ReconfigureComputeResourceRequestType.from_json(json)
# print the JSON string representation of the object
print ReconfigureComputeResourceRequestType.to_json()

# convert the object into a dict
reconfigure_compute_resource_request_type_dict = reconfigure_compute_resource_request_type_instance.to_dict()
# create an instance of ReconfigureComputeResourceRequestType from a dict
reconfigure_compute_resource_request_type_form_dict = reconfigure_compute_resource_request_type.from_dict(reconfigure_compute_resource_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


