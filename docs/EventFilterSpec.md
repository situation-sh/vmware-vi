# EventFilterSpec

Event filter used to query events in the history collector database.  The client creates an event history collector with a filter specification, then retrieves the events from the event history collector. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**EventFilterSpecByEntity**](EventFilterSpecByEntity.md) |  | [optional] 
**time** | [**EventFilterSpecByTime**](EventFilterSpecByTime.md) |  | [optional] 
**user_name** | [**EventFilterSpecByUsername**](EventFilterSpecByUsername.md) |  | [optional] 
**event_chain_id** | **int** | The filter specification for retrieving events by chain ID.  If the property is not set, events with any chain ID are collected.  | [optional] 
**alarm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**scheduled_task** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**disable_full_message** | **bool** | Flag to specify whether or not to prepare the full formatted message for each event.  If the property is not set, the collected events do not include the full formatted message.  | [optional] 
**category** | **List[str]** | This property, if set, limits the set of collected events to those associated with the specified category.  If the property is not set, events are collected regardless of their association with any category. \&quot;category\&quot; here is the same as Event.severity.  | [optional] 
**type** | **List[str]** | Deprecated as of vSphere API 4.0, use *EventFilterSpec.eventTypeId* instead.  This property, if set, limits the set of collected events to those specified types.  If the property is not set, events are collected regardless of their types.  | [optional] 
**tag** | **List[str]** | This property, if set, limits the set of filtered events to those that have it.  If not set, or the size of it 0, the tag of an event is disregarded. A blank string indicates events without tags.  ***Since:*** vSphere API 4.0  | [optional] 
**event_type_id** | **List[str]** | This property, if set, limits the set of collected events to those specified types.  Note: if both *EventFilterSpec.eventTypeId* and *EventFilterSpec.type* are specified, an exception may be thrown by *EventManager.CreateCollectorForEvents*.  The semantics of how eventTypeId matching is done is as follows: - If the event being collected is of type *EventEx*   or *ExtendedEvent*, then we match against the   &lt;code&gt;eventTypeId&lt;/code&gt; (for &lt;code&gt;EventEx&lt;/code&gt;) or   &lt;code&gt;eventId&lt;/code&gt; (for &lt;code&gt;ExtendedEvent&lt;/code&gt;) member of the Event. - Otherwise, we match against the type of the Event itself.    If neither this property, nor &lt;code&gt;type&lt;/code&gt;, is set, events are collected regardless of their types.  ***Since:*** vSphere API 4.0  | [optional] 
**max_count** | **int** | This property, if set, specifies the maximum number of returned events.  If unset, the default maximum number will be used. Using this property with *EventManager.CreateCollectorForEvents* is more efficient than a call to *HistoryCollector.SetCollectorPageSize*.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.event_filter_spec import EventFilterSpec

# TODO update the JSON string below
json = "{}"
# create an instance of EventFilterSpec from a JSON string
event_filter_spec_instance = EventFilterSpec.from_json(json)
# print the JSON string representation of the object
print EventFilterSpec.to_json()

# convert the object into a dict
event_filter_spec_dict = event_filter_spec_instance.to_dict()
# create an instance of EventFilterSpec from a dict
event_filter_spec_form_dict = event_filter_spec.from_dict(event_filter_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


