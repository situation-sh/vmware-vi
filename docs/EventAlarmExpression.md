# EventAlarmExpression

An alarm expression that uses the event stream to trigger the alarm.  This alarm is triggered when an event matching this expression gets logged.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comparisons** | [**List[EventAlarmExpressionComparison]**](EventAlarmExpressionComparison.md) | The attributes/values to compare.  ***Since:*** vSphere API 4.0  | [optional] 
**event_type** | **str** | Deprecated use &lt;code&gt;eventTypeId&lt;/code&gt; instead.  The type of the event to trigger the alarm on.  ***Since:*** VI API 2.5  | 
**event_type_id** | **str** | The eventTypeId of the event to match.  The semantics of how eventTypeId matching is done is as follows: - If the event being matched is of type *EventEx*   or *ExtendedEvent*, then we match this value   against the &lt;code&gt;eventTypeId&lt;/code&gt; (for &lt;code&gt;EventEx&lt;/code&gt;) or   &lt;code&gt;eventId&lt;/code&gt; (for &lt;code&gt;ExtendedEvent&lt;/code&gt;) member of the Event. - Otherwise, we match it against the type of the Event itself.    Either &lt;code&gt;eventType&lt;/code&gt; or &lt;code&gt;eventTypeId&lt;/code&gt; _must_ be set.  ***Since:*** VI API 2.5  | [optional] 
**object_type** | **str** | Name of the type of managed object on which the event is logged.  An event alarm defined on a *ManagedEntity* is propagated to child entities in the VirtualCenter inventory depending on the value of this attribute. If objectType is any of the following, the alarm is propagated down to all children of that type: - A datacenter: *Datacenter*. - A cluster of host systems: *ClusterComputeResource*. - A single host system: *HostSystem*. - A resource pool representing a set of physical resources on a single host:   *ResourcePool*. - A virtual machine: *VirtualMachine*. - A datastore: *Datastore*. - A network: *Network*. - A distributed virtual switch: *DistributedVirtualSwitch*.    If objectType is unspecified or not contained in the above list, the event alarm is not propagated down to child entities in the VirtualCenter inventory.  It is possible to specify an event alarm containing two (or more) different EventAlarmExpression&#39;s which contain different objectTypes. In such a case, the event is propagated to all child entities with specified type(s).  ***Since:*** vSphere API 4.0  | [optional] 
**status** | [**ManagedEntityStatusEnum**](ManagedEntityStatusEnum.md) |  | [optional] 

## Example

```python
from vmware_vi.models.event_alarm_expression import EventAlarmExpression

# TODO update the JSON string below
json = "{}"
# create an instance of EventAlarmExpression from a JSON string
event_alarm_expression_instance = EventAlarmExpression.from_json(json)
# print the JSON string representation of the object
print EventAlarmExpression.to_json()

# convert the object into a dict
event_alarm_expression_dict = event_alarm_expression_instance.to_dict()
# create an instance of EventAlarmExpression from a dict
event_alarm_expression_form_dict = event_alarm_expression.from_dict(event_alarm_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


