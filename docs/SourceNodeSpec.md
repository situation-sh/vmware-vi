# SourceNodeSpec

The SourceNodeSpec class defines specification of the source node that is used to initiate the configuration or deployment for VCHA.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**management_vc** | [**ServiceLocator**](ServiceLocator.md) |  | 
**active_vc** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.source_node_spec import SourceNodeSpec

# TODO update the JSON string below
json = "{}"
# create an instance of SourceNodeSpec from a JSON string
source_node_spec_instance = SourceNodeSpec.from_json(json)
# print the JSON string representation of the object
print SourceNodeSpec.to_json()

# convert the object into a dict
source_node_spec_dict = source_node_spec_instance.to_dict()
# create an instance of SourceNodeSpec from a dict
source_node_spec_form_dict = source_node_spec.from_dict(source_node_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


