# PerfStatsTypeEnum

Indicates the type of statistical measurement that a counter&#146;s value represents.  Valid types are &#147;absolute&#148;, &#147;delta&#148;, or &#147;rate&#148;.  Possible values: - `absolute`: Represents an actual value, level, or state of the counter.      For   example, the &#147;uptime&#148; counter (**system** group)   represents the actual number of seconds since startup. The   &#147;capacity&#148; counter represents the actual configured size   of the specified datastore. In other words, number of samples,   samplingPeriod, and intervals have no bearing on an   &#147;absolute&#148; counter&#147;s value. - `delta`: Represents an amount of change for the counter during the *PerfInterval.samplingPeriod* as compared to the previous   *interval*.      The first sampling interval - `rate`: Represents a value that has been normalized over the *PerfInterval.samplingPeriod*, enabling values for the same   counter type to be compared, regardless of interval.      For example,   the number of reads per second. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


