package example;

/* metamodel_version: 1.12.0 */
/* version: 1.5.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A Windows critical section is a Windows object that provides synchronization similar to that provided by a mutex object, except that a critical section can be used only by the threads of a single process. Critical section objects cannot be shared across processes. Event, mutex, and semaphore objects can also be used in a single-process application, but critical section objects provide a slightly faster, more efficient mechanism for mutual-exclusion synchronization (a processor-specific test and set instruction). Like a mutex object, a critical section object can be owned by only one thread at a time, which makes it useful for protecting a shared resource from simultaneous access. Unlike a mutex object, there is no way to tell whether a critical section has been abandoned. [based on https://docs.microsoft.com/en-us/windows/win32/sync/critical-section-objects]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class WindowsCriticalSection extends ObservableObject {



}