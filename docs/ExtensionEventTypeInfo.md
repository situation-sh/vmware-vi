# ExtensionEventTypeInfo

This data object type describes event types defined by the extension.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | The ID of the event type.  Should follow java package naming conventions for uniqueness.  ***Since:*** VI API 2.5  | 
**event_type_schema** | **str** | Optional XML descriptor for the EventType.  The structure of this descriptor is:       &lt;EventType&gt;        &lt;eventTypeID&gt;eventID&lt;/eventTypeID&gt;        &lt;description&gt;Optional description for event eventID&lt;/description&gt;        &lt;-- Optional arguments: --&gt;        &lt;arguments&gt;           &lt;-- Zero or more of: --&gt;           &lt;argument&gt;             &lt;name&gt;argName&lt;/name&gt;             &lt;type&gt;argtype&lt;/name&gt;           &lt;/argument&gt;        &lt;/arguments&gt;      &lt;/EventType&gt; where _argtype_ can be one of the following: - This is an example list and should be considered as incomplete. &lt;!-- --&gt; - Primitive types:   - _string_   - _bool_   - _int_   - _long_   - _float_   - _moid_ - Entity reference types:   - _vm_   - _host_   - _resourcepool_   - _computeresource_   - _datacenter_   - _datastore_   - _network_   - _dvs_      ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.extension_event_type_info import ExtensionEventTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ExtensionEventTypeInfo from a JSON string
extension_event_type_info_instance = ExtensionEventTypeInfo.from_json(json)
# print the JSON string representation of the object
print ExtensionEventTypeInfo.to_json()

# convert the object into a dict
extension_event_type_info_dict = extension_event_type_info_instance.to_dict()
# create an instance of ExtensionEventTypeInfo from a dict
extension_event_type_info_form_dict = extension_event_type_info.from_dict(extension_event_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


