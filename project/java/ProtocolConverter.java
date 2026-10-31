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
  A protocol converter is a device that converts from one protocol to another (e.g. SD to USB, SATA to USB, etc.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ProtocolConverter extends Device {



}