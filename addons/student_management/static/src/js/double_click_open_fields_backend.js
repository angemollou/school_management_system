/** @odoo-module **/

import { registry } from "@web/core/registry";
import { ListRenderer } from "@web/views/list/list_renderer";
import { listView } from "@web/views/list/list_view";
// const SINGLE_CLICK_EDIT_TIMEOUT = 175;

export class DblClickOpenListRenderer extends ListRenderer {
  /**
   * The purpose of this extension is to allow user to open
   * a one2many editable list record in a double click.
   *
   * @override
   */
  setup() {
    super.setup();
    // Handle double click manually
    // this._clickCount = 0;
  }
  async onCellClicked(record, column, ev) {
    // Handle double click manually
    // if (this._clickCount === 0) {
    //   this.rowClickedTimer = setTimeout(() => {
    //     super.onCellClicked(record, column, ev);
    //     this._clickCount = 0;
    //   }, SINGLE_CLICK_EDIT_TIMEOUT);
    //   this._clickCount++;
    // } else if (this._clickCount === 1) {
    //   if (!this.props.archInfo.noOpen) {
    //     this.props.openRecord(record);
    //   }
    //   clearTimeout(this.rowClickedTimer);
    //   this._clickCount = 0;
    // }
    // Handle double click natively
    if (ev.detail === 1) {
      // it was a single click
      super.onCellClicked(record, column, ev);
    } else if (ev.detail === 2) {
      // it was a double click
      this.props.openRecord(record);
    }
  }
}

export const DblClickOpenListView = {
  ...listView,
  Renderer: DblClickOpenListRenderer,
};

registry.category("views").add("daysum_tree", DblClickOpenListView);
