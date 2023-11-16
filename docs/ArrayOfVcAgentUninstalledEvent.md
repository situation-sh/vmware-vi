# ArrayOfVcAgentUninstalledEvent

A boxed array of *VcAgentUninstalledEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VcAgentUninstalledEvent]**](VcAgentUninstalledEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vc_agent_uninstalled_event import ArrayOfVcAgentUninstalledEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVcAgentUninstalledEvent from a JSON string
array_of_vc_agent_uninstalled_event_instance = ArrayOfVcAgentUninstalledEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVcAgentUninstalledEvent.to_json()

# convert the object into a dict
array_of_vc_agent_uninstalled_event_dict = array_of_vc_agent_uninstalled_event_instance.to_dict()
# create an instance of ArrayOfVcAgentUninstalledEvent from a dict
array_of_vc_agent_uninstalled_event_form_dict = array_of_vc_agent_uninstalled_event.from_dict(array_of_vc_agent_uninstalled_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


