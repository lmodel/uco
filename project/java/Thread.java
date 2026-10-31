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
  A semi-ordered array of items, that can be present in multiple copies. Implementation of a UCO Thread is similar to a Collections Ontology List, except a Thread may fork and merge - that is, one of its members may have two or more direct successors, and two or more direct predecessors.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Thread extends UcoThing {

  private URI id;
  private List<ThreadItem> item;
  private List<ThreadItem> threadOriginItem;
  private List<ThreadItem> threadTerminalItem;
  private Integer coSize;


}